function inorder_successor(root, node) {
	/**
	 * If we have a right subtree (right node),
	 * then the minimum value in that subtree is
	 * the in-order successor.
	 */
	if (node.right) {
		let aNode = node.right
		let successor = aNode

		while (aNode.left) {
			successor = aNode.left
			aNode = aNode.left
		}

		return successor
	}

	/**
	 * If there is no larger value, than we have to travel
	 * from the root down until we find the successor.
	 */
	let successor = undefined
	while (root) {
		/**
		 * If the value is larger, than this is a possible
		 * successor. Track it, and also go down the left subtree
		 * to identify a possibly smaller, but still larger value.
		 */
		if (root.value > node.value) {
			successor = root
			root = root.left
		}

		/**
		 * If the value is smaller, than we need to traverse
		 * down the right subtree to get a larger value.
		 */
		else if (root.value < node.value) {
			root = root.right
		}

		/**
		 * If we are back at our original node value, break the loop.
		 * Traversing any further will give us minimal values.
		 */
		else {
			break;
		}
	}

	return successor
}

class Node {
	constructor(value) {
		this.value = value;
	}
}

/**
 *          10
 *      6        18
 *    4   8   15    21
 */
rootNode = new Node(10);
rootNode.left = new Node(6);
rootNode.right = new Node(18);

rootNode.left.left = new Node(4);
rootNode.left.right = new Node(8);

rootNode.right.left = new Node(15);
rootNode.right.right = new Node(21);

const assert = require('assert');
// Successor of 10 is 15
assert.strictEqual(inorder_successor(rootNode, rootNode), rootNode.right.left);
// Successor of 4 is 6
assert.strictEqual(inorder_successor(rootNode, rootNode.left.left), rootNode.left);
// Successor of 8 is 10
assert.strictEqual(inorder_successor(rootNode, rootNode.left.right), rootNode);
// Successor of 18 is 21
assert.strictEqual(inorder_successor(rootNode, rootNode.right), rootNode.right.right);
