#include<stdio.h>
#include<stdlib.h>
typedef struct ListNode {
	int element;
	struct ListNode *next;
}ListNode,*ListNodePtr;
int main()
{
	ListNodePtr Head = (ListNodePtr)malloc(sizeof(ListNode));
	ListNodePtr fixPtr = Head;
	Head->next = NULL;
	ListNodePtr P = Head;
	int i = 0;
	printf("init:%x\n",Head);
	/*
	初始化链表,浪费了头结点。仅作为头指针
	*/
	for(;i<10;i++)//0--9
	{
		P->next = (ListNodePtr)malloc(sizeof(ListNode));
		P->next->next = NULL;
		P->next->element = i;
		P = P->next;
		
		
	}
	printf("init2:%x\n",Head);
	/*
	遍历链表
	*/
	ListNodePtr Ptr = Head;
	Ptr = Ptr->next;
	while(Ptr != NULL)
	{
		printf("%d\t",Ptr->element);
		Ptr = Ptr->next;
	}
	printf("iteror:%x\n",Head);
	/*
	逆转链表
	*/
	/* Ptr = Head;//Ptr是头指针
	Head = NULL;//变量Head指向空
	while(Ptr != NULL)//不为空
	{
		ListNodePtr Q = Ptr->next;//Q指向首node，暂存
		Ptr->next = Head;//第一次指向空
		Head = Ptr;//Head恢复
		Ptr = Q;//移动工作指针
	
	}
	*/
	
	
	Ptr = Head->next;//ptr point to the first node 工作指针
	Head->next = NULL;//head->next point to NULL
	while(Ptr != NULL)
	{
		ListNodePtr Q = Ptr->next;//暂存Ptr->next
		Ptr->next = Head->next;
		Head->next = Ptr;
		Ptr = Q;
		/*
		一环扣一环的方法
		*/
		
		
	}
	
	/*Ptr = Head;
	Head = NULL;
	while(Ptr)
	{
		ListNodePtr Q = Ptr->next;
		Ptr->next = Head;
		Head = Ptr;
		Ptr = Q;
	}*/
	printf("anfter-reverse:%x\n",Head);
	
	
	/*
	遍历链表
	*/
	Ptr = Head;
	Ptr = Ptr->next;
	while(Ptr != NULL)
	{
		printf("%d\t",Ptr->element);
		Ptr = Ptr->next;
	}
	
	return 0;
}