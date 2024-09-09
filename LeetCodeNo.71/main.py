#  The key idea here is to use a stack for append and pop (when there is a ..).

class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = path.split('/')
        dir_list = [x for x in dir_list if x != '']
        print(dir_list)

        processed_dir_list = []

        for ele in range(0, len(dir_list)):
            if dir_list[ele] == '.':
                pass
            elif dir_list[ele] == '..':
                if len(processed_dir_list) > 0:
                    processed_dir_list.pop()
            else:
                processed_dir_list.append(dir_list[ele])
        print(processed_dir_list)
        ret = '/' + '/'.join(processed_dir_list)
        return ret