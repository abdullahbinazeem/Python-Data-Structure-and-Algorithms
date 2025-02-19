class TreeNode:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def print_tree(self, property, h):
        if property == 'both':
            value = self.name + " (" + self.role + ")"
        elif property == 'name':
            value = self.name
        else:
            value = self.role

        spaces = " " * 4 * h
        prefix = spaces + ("|__" if self.parent else "")

        print(prefix+value)

        for child in self.children:
            child.print_tree(property, h+1)
        
def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Abdullah","Infrastructure Head")
    infra_head.add_child(TreeNode("Yahya","Cloud Manager"))
    infra_head.add_child(TreeNode("Mustafa", "App Manager"))

    cto = TreeNode("Yusuf", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Ameer","HR Head")

    hr_head.add_child(TreeNode("Hamza","Recruitment Manager"))
    hr_head.add_child(TreeNode("Muhammad", "Policy Manager"))

    ceo = TreeNode("Farhan", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name",0)
    root_node.print_tree("designation",0)
    root_node.print_tree("both",0)