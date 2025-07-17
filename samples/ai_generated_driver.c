#include <linux/module.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/kernel.h> 

#define DEVICE_NAME "mychardev"
#define BUFFER_SIZE 1024

static int major;
static char device_buffer[BUFFER_SIZE];
static int open_count = 0;

static int dev_open(struct inode *inode, struct file *file) {
    open_count++;
    printk(KERN_INFO "Device opened %d time(s)\n", open_count);
    return 0;
}

static int dev_release(struct inode *inode, struct file *file) {
    printk(KERN_INFO "Device released\n");
    return 0;
}

static ssize_t dev_read(struct file *file, char __user *buf, size_t len, loff_t *offset) {
    int bytes_to_copy = min(len, (size_t)BUFFER_SIZE);
    if (copy_to_user(buf, device_buffer, bytes_to_copy)) {
        return -EFAULT;
    }
    return bytes_to_copy;
}

static ssize_t dev_write(struct file *file, const char __user *buf, size_t len, loff_t *offset) {
    int bytes_to_copy = min(len, (size_t)BUFFER_SIZE);
    if (copy_from_user(device_buffer, buf, bytes_to_copy)) {
        return -EFAULT;
    }
    return bytes_to_copy;
}

static struct file_operations fops = {
    .open = dev_open,
    .release = dev_release,
    .read = dev_read,
    .write = dev_write
};

static int __init mydriver_init(void) {
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0) {
        printk(KERN_ALERT "Device registration failed\n");
        return major;
    }
    printk(KERN_INFO "Device registered with major number %d\n", major);
    return 0;
}

static void __exit mydriver_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "Device unregistered\n");
}

module_init(mydriver_init);
module_exit(mydriver_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("AI Model");
MODULE_DESCRIPTION("Sample Character Driver");
