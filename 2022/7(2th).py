                        
                        
                        # TODO try to implement it yourself 


#             else:
#                 output = ((l.split()[0] , l.split()[1]))
#                 directories[list(directories.keys())[-1]].append(output)
#         sub_dirs = get_all_sub_directories('/')
#         # directories size
#         sub_sub_dir = {}
#         for k, v in sub_dirs.items():
#             sub_sub_dir[k] = []
#             for i in v:
#                 sub_sub_dir[k] += get_all_sub_directories(i)
        
#         for k, v in sub_sub_dir.items():
#             dir_size[k] = get_dir_size(k)
#             for i in v:
#                 dir_size[k] += get_dir_size(i)

#     print(sub_sub_dir['bsjbvff'])
#     # print(directories['/'])
#     print(sum([v for _,v in dir_size.items() if v <= most_size]))



# def get_all_sub_directories(root:str):
#     # TODO implement this without recursion. hint:(for loop on directoriess)
#     global directories
#     sub_dirs = {}
#     def recurse(current):
#         sub_dirs[current] = []
#         if directories.get(current):
#             for v in directories[current]:
#                 if 'dir' not in v[0]:
#                     continue   
#                 else:
#                     sub_dirs[current].append(v[1])

#         return [recurse(v) for v in sub_dirs[current]]
#     recurse(root)
#     return sub_dirs

# def get_dir_size(directory):
#     global directories
#     total = 0
#     if directory:
#         if directories.get(directory):
#             for v in directories[directory]:
#                 total += int(v[0]) if v[0].isdigit() else 0
        
#     return total

# print(get_all_sub_directories('/'))
# print(get_dir_size('bsjbvff'))
# print(sum([get_dir_size(v[0]) for v in get_all_sub_directories('/')]))