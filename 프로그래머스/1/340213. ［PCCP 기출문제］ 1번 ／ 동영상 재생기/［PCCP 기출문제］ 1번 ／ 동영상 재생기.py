def change_to_sec(time):
        minutes, seconds = time.split(':')
        time = int(minutes)*60 + int(seconds)
        return time
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = change_to_sec(video_len)
    pos = change_to_sec(pos)
    op_start = change_to_sec(op_start)
    op_end = change_to_sec(op_end)
        
    for i in range(len(commands)):
        if op_start <= pos <= op_end:
            pos = op_end
        
        if commands[i]=='prev':
            if pos < 10:
                pos = 0
            else:
                pos = pos - 10
        elif commands[i]=='next':
            if (video_len-pos)<10:
                pos = video_len
            else:
                pos = pos + 10
            
    if op_start <= pos <= op_end:
        pos = op_end
    answer = str(f"{pos//60:02}")+':'+str(f"{pos%60:02}")
    return answer