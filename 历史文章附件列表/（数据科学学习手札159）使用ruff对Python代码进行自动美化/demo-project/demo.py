import os
# 提取目标路径下各文件的创建时间及最近修改时间
target_path ="target_path"
# 需要排除的文件拓展名
ignore_file_types =['.mp4','.avi', '.rmvb' 
                   ]
# 结果元组格式：(文件名，创建时间，最近修改时间)
files=[(file,os.path.getctime(os.path.join(target_path,file)),os.path.getmtime(
    os.path.join(target_path,file) )) for file in os.listdir(target_path)
# 判断当前文件名是否为文件，且不在排除拓展名列表中
if os.path.isfile(os.path.join(target_path, file)) and 
not any(file.endswith(ext) for ext in ignore_file_types
                                                               )]