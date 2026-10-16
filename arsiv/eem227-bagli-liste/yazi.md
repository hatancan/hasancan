---
baslik: EEM227 Veri Yapıları: Java ile Bağlı Liste (Node Zinciri)
ozet: EEM227 Veri Yapıları dersinin bağlı liste (linked list) örneği: Node sınıfı, elle kurulan düğüm zinciri, addToLast, addToFront ve removeFirst metotlarıyla MyLinkedList; düğümleri dışarıdan gizleyen ikinci sürüm.
---

Bu yazı, Başkent Üniversitesi **EEM227 Veri Yapıları** dersinde (Kasım 2013) işlenen bağlı liste (linked list) örneğinin Java kodlarını içeriyor. Konu, izlencenin 3. haftasındaki "Linked Lists – Java programlama dilinde kullanımı". Örnek adım adım ilerliyor: önce tek bir düğüm, sonra elle bağlanan bir zincir, sonra bu zinciri yöneten bir liste sınıfı. Orijinal BlueJ projesi yazının sonunda 7z arşivi olarak indirilebilir.

## Düğüm: Node

Her düğüm bir değer ve bir sonraki düğümü gösteren bir referans taşır.

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

## Elle kurulan zincir

Üç düğüm oluşturulup birbirine bağlanıyor: 3 → 5 → 7.

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

## Liste sınıfı: MyLinkedList

Zincirin başını ve sonunu tutan, eleman sayısını sayan bir sınıf. Sona eklemede son düğümün `next`'i yeni düğüme bağlanıyor; başa eklemede yeni düğümün `next`'i eski ilk düğüme bağlanıyor.

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

## Düğümleri gizleyen sürüm: MyLinkedListHideNodeInt

İkinci sürümde liste dışarıya `Node` değil, doğrudan `int` alıyor; düğüm oluşturma işi sınıfın içine saklanıyor. Kullanıcı artık bağlı listenin iç yapısını bilmek zorunda değil. Bu sürümde ilk elemanı silen `removeFirst` de var.

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

`removeFirst` ilk düğümü silmek için yalnızca `firstNode`'u bir sonrakine kaydırıyor; eski ilk düğüme artık hiçbir referans kalmadığı için çöp toplayıcı onu temizliyor. Bağlı listenin diziden farkı tam olarak bu: başa ekleme ve baştan silme, eleman sayısından bağımsız olarak sabit sürede yapılabiliyor.
