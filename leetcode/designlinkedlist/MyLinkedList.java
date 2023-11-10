package leetcode.designlinkedlist;

class MyLinkedList {
    class Node {
        Node next;
        int value;
        Node() {
            next = null;
            value = 0;
        }
    }

    Node head;

    public MyLinkedList() {
        head = null;
    }

    public int get(int index) {
        Node current = head;
        for (int i = 0; i < index; i++) {
            if (current == null) {
                return -1; // or throw an exception
            }
            current = current.next;
        }

        if (current == null) {
            return -1; // or throw an exception
        }

        return current.value;
    }

    public void addAtHead(int val) {
        Node node = new Node();
        node.value = val;
        node.next = head;
        head = node;
    }
    
    public void addAtTail(int val) {
        Node current = head;
        if (current == null) {
            addAtHead(val);
            return;
        }

        while (current.next != null)
            current = current.next;
        Node node = new Node();
        node.value = val;
        current.next = node;
    }

    public void addAtIndex(int index, int val) {
        if (index < 0) {
            return; // index is invalid, do nothing
        }

        if (index == 0) {
            addAtHead(val);
            return;
        }

        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            if (current == null) {
                return; // index is invalid, do nothing
            }
            current = current.next;
        }

        if (current != null) {
            Node node = new Node();
            node.value = val;
            node.next = current.next;
            current.next = node;
        }
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0) {
            return; // index is invalid, do nothing
        }

        if (index == 0) {
            head = head.next;
            return;
        }

        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            if (current == null || current.next == null) {
                return; // index is invalid, do nothing
            }
            current = current.next;
        }

        if (current != null && current.next != null) {
            current.next = current.next.next;
        }
    }
}