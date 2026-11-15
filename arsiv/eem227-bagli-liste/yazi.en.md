---
baslik: EEM227 Data Structures: Linked List in Java (Node Chain)
ozet: A linked list example from the EEM227 Data Structures course: the Node class, a manually built chain of nodes, MyLinkedList with the addToLast, addToFront and removeFirst methods; and a second version that hides the nodes from the outside.
---

This post contains the Java code for the linked list example covered in the **EEM227 Data Structures** course at Başkent University (November 2013). The topic corresponds to week 3 of the syllabus, "Linked Lists – Usage in the Java programming language". The example proceeds step by step: first a single node, then a manually linked chain, then a list class that manages this chain. The original BlueJ project can be downloaded as a 7z archive at the end of the post.

## Node: Node

Each node carries a value and a reference pointing to the next node.

```java
public class Node
{
    private int value;
    private Node next;

    public int getValue()
    {
        return value;
    }
    public void setValue(int pValue)
    {
        value = pValue;
    }

    public Node getNext()
    {
        return next;
    }

    public void setNext(Node pNode)
    {
        next = pNode;
    }
}
```

## Manually built chain

Three nodes are created and linked together: 3 → 5 → 7.

```java
public class NodeChainTest1
{
    public static void main()
    {
        Node n1 = new Node();
        n1.setValue(3);

        Node n2 = new Node();
        n2.setValue(5);

        Node n3 = new Node();
        n3.setValue(7);

        n1.setNext(n2);
        n2.setNext(n3);
    }
}
```

## List class: MyLinkedList

A class that keeps track of the head and tail of the chain and counts the number of elements. When adding to the end, the `next` of the last node is linked to the new node; when adding to the front, the `next` of the new node is linked to the old first node.

```java
public class MyLinkedList
{
    private Node firstNode;
    private Node lastNode;
    private int nodeCount = 0;

    public void addToLast(Node node)
    {
        if (nodeCount == 0)
        {
            firstNode = node;
            lastNode = node;
            nodeCount++;
        }
        else
        {
          Node temp = lastNode;
          temp.setNext(node);
          lastNode = node;
          nodeCount++;
        }
    }

    public Node getFirstNode()
    {
        return firstNode;
    }
    public Node getLastNode()
    {
        return lastNode;
    }
    public int size()
    {
        return nodeCount;
    }

    public void addToFront(Node node)
    {
        if (nodeCount == 0)
        {
            firstNode = node;
            lastNode = node;
            nodeCount++;
        }
        else
        {
            Node temp = firstNode;
            node.setNext(firstNode);
            firstNode = node;
            nodeCount++;
        }
    }
}
```

## Version that hides the nodes: MyLinkedListHideNodeInt

In the second version, the list accepts a plain `int` from the outside rather than a `Node`; the job of creating nodes is hidden inside the class. The user no longer needs to know the internal structure of the linked list. This version also includes `removeFirst`, which deletes the first element.

```java
public class MyLinkedListHideNodeInt
{
    private Node firstNode;
    private Node lastNode;
    private int nodeCount = 0;

    public void addToLast(int sayi)
    {
        Node node = new Node();
        node.setValue(sayi);

        if (nodeCount == 0)
        {
            firstNode = node;
            lastNode = node;
            nodeCount++;
        }
        else
        {
          Node temp = lastNode;
          temp.setNext(node);
          lastNode = node;
          nodeCount++;
        }
    }

    public int size()
    {
        return nodeCount;
    }

    public void addToFront(int sayi)
    {
        Node node = new Node();
        node.setValue(sayi);

        if (nodeCount == 0)
        {
            firstNode = node;
            lastNode = node;
            nodeCount++;
        }
        else
        {
            Node temp = firstNode;
            node.setNext(firstNode);
            firstNode = node;
            nodeCount++;
        }
    }

    public void removeFirst()
    {
        if (nodeCount == 0)
        {
            return;
        }
        else if (nodeCount == 1)
        {
            nodeCount--;
            firstNode = null;
            lastNode = null;
        }
        else
        {
            Node  newFirstNode = firstNode.getNext();
            firstNode = newFirstNode;
            nodeCount--;
        }
    }
}
```

To delete the first node, `removeFirst` simply shifts `firstNode` to the next one; since no references to the old first node remain, the garbage collector cleans it up. This is exactly how a linked list differs from an array: adding to the front and removing from the front can be done in constant time, independent of the number of elements.
