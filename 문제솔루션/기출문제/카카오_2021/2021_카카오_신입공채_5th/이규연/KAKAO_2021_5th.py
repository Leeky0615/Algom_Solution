def change_sec(time):
    hour, min, sec = time.split(':')
    return int(hour) * 60 * 60 + int(min) * 60 + int(sec)


def solution(play_time, adv_time, logs):
    answer = ''
    # play_time -> 초 변환
    play_time_sec = change_sec(play_time)

    # adv_time -> 초 변환
    adv_time_sec = change_sec(adv_time)
    total_time = [0 for _ in range(play_time_sec + 1)]
    # logs -> 초 변환, 끝나는 시간을 기준으로 정렬
    for log in logs:
        log_start, log_end = log.split("-")
        start = change_sec(log_start)
        end = change_sec(log_end)
        total_time[start] += 1
        total_time[end] -= 1

    for i in range(1, play_time_sec):
        total_time[i] += total_time[i - 1]

    current_time = sum(total_time[:adv_time_sec])

    max_time = current_time
    max_time_idx = 0
    for i in range(adv_time_sec, play_time_sec):
        current_time = current_time + total_time[i] - total_time[i - adv_time_sec]
        if current_time > max_time:
            max_time = current_time
            max_time_idx = i - adv_time_sec + 1
    answer = '%02d:%02d:%02d' % (max_time_idx / 3600, max_time_idx / 60 % 60, max_time_idx % 60)
    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14",
        "00:40:31-01:00:00",
        "00:25:50-00:48:29",
        "01:30:59-01:53:29",
        "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
