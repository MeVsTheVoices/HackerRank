package leetcode.designlinkedlist;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolutionTest {
    @Test
    public void testAddAtHead() {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtHead(2);
        linkedList.addAtHead(3);
        linkedList.addAtHead(4);
        linkedList.addAtHead(5);

        int[] result = new int[] {5, 4, 3, 2, 1};
        for (int i = 0;i < result.length; i++) {
            assertEquals(result[i], linkedList.get(i));
        }
    }

    @Test
    public void testAddAtTail() {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.addAtTail(1);
        linkedList.addAtTail(2);
        linkedList.addAtTail(3);
        linkedList.addAtTail(4);
        linkedList.addAtTail(5);

        int[] result = new int[] {1, 2, 3, 4, 5};
        for (int i = 0;i < result.length; i++) {
            assertEquals(result[i], linkedList.get(i));
        }
    }

    @Test
    public void testAddAtIndex() {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtHead(2);
        linkedList.addAtHead(3);
        linkedList.addAtHead(4);
        linkedList.addAtHead(5);
        linkedList.addAtIndex(2, 6);
        linkedList.addAtIndex(0, 7);
        linkedList.addAtIndex(6, 8);

        int[] result = new int[] {7, 5, 4, 6, 3, 2, 8, 1};
        for (int i = 0;i < result.length; i++) {
            assertEquals(result[i], linkedList.get(i));
        }
    }

    @Test
    public void testDeleteAtIndex() {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtHead(2);
        linkedList.addAtHead(3);
        linkedList.addAtHead(4);
        linkedList.addAtHead(5);
        linkedList.addAtIndex(2, 6);
        linkedList.addAtIndex(0, 7);
        linkedList.addAtIndex(6, 8);
        // before  int[] result = new int[] {7, 5, 4, 6, 3, 2, 8, 1};
        linkedList.deleteAtIndex(0);
        // {5, 4, 6, 3, 2, 8, 1};
        linkedList.deleteAtIndex(6);
        // {5, 4, 6, 3, 2, 8};
        linkedList.deleteAtIndex(2);
        // {5, 4, 3, 2, 8};

        int[] result = new int[] {5, 4, 3, 2, 8};
        for (int i = 0;i < result.length; i++) {
            assertEquals(result[i], linkedList.get(i));
        }
    }
}
