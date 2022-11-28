#include <iostream>
struct Node {
    int data;
    Node *link;
};
using namespace std;
typedef Node* nodePtr;
void insert(nodePtr& head, int data);


void insert(nodePtr& head, int data) {
    //creating just the pointer and not structure object
    nodePtr temp;
    temp = new Node;
    temp ->data = data;
    temp ->link = head;
    head = temp;
}


int main() {
    nodePtr head;
    head = new Node;
    head ->data = 20;
    head ->link = nullptr;
    cout<<head->data<<endl;
    insert(head, 24);
    cout<<head->data<<endl;

}