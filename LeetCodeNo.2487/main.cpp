/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    // Check all nodes right to currentNode. Return true if found a bigger val.
    bool checkAllRightNodes(ListNode* currentNode) {
        int currentVal = currentNode->val;

        while(currentNode->next != nullptr) {
            if (currentNode->next->val > currentVal) {
                return true;
            }
            currentNode = currentNode->next;
        }
        return false;
    }
    // Remove current node.
    void removeCurrentNode(ListNode* currentNode, ListNode* formerNode) {
        formerNode->next = currentNode->next;
    }
public:
    // My solution. Stupid. This causes time limit exceeded error in runtime. 
    ListNode* removeNodes_my(ListNode* head) {

        if (head == nullptr || head->next == nullptr)
            return head;

        // Fist, check from head. Until reaching a node where no bigger val can be found to its right.
        // This node will be the head of our final return.
        while(checkAllRightNodes(head)) {
            head = head->next;
        }

        ListNode* currentNode = head->next;
        ListNode* formerNode = head;

        while (currentNode->next != nullptr) {
            if (checkAllRightNodes(currentNode)) {
                removeCurrentNode(currentNode, formerNode);
                currentNode = currentNode->next;
            }
            else {
                formerNode = currentNode;
                currentNode = currentNode->next;
            }
        }

        return head;
    }

    // Other people's solution.
    ListNode* removeNodes(ListNode* head) {
        ListNode* cur = head;
        stack<ListNode*> stack;
        
        while (cur != nullptr) {
            // Keep pop until the top stack val is >= current node value.
            while (!stack.empty() && stack.top()->val < cur->val) {
                stack.pop();
            }
            stack.push(cur);
            cur = cur->next;
        }
        
        // Reconstruct all nodes in stack by reassigning their next value.
        ListNode* nxt = nullptr;
        while (!stack.empty()) {
            cur = stack.top();
            stack.pop();
            cur->next = nxt;
            nxt = cur;
        }
        
        return cur;
    }
};