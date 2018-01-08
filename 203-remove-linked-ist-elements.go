package removeElements

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	fakeHead := &ListNode{Val: 0, Next: head}
	ptr := fakeHead
	for ptr != nil && ptr.Next != nil {
		if ptr.Next.Val == val {
			ptr.Next = ptr.Next.Next
		} else {
			ptr = ptr.Next
		}
	}

	return fakeHead.Next
}
