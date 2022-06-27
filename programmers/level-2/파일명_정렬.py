from functools import cmp_to_key
class File(object):
    def __init__(
        self,
        head: str,
        number: str,
        tail: str,
        org_idx: int,
    ) -> None:
        self.head = head
        self.number = number
        self.tail = tail
        self.org_idx = org_idx


def cmp(x1:File, x2:File):
    if x1.head.lower() > x2.head.lower():
        return 1
    elif x1.head.lower() < x2.head.lower():
        return -1
    else:
        if int(x1.number) > int(x2.number):
            return 1
        elif int(x1.number) < int(x2.number):
            return -1
        else:
            if x1.org_idx > x2.org_idx:
                return 1
            elif x1.org_idx < x2.org_idx:
                return -1
            else:
                return 0

def solution(files):
    answer = []
    for org_idx, file in enumerate(files):
        section = False
        start, end = 0, 0
        for i in range(len(file)):
            if file[i].isdigit() and not section:
                start = i
                section = True
            if section and not file[i].isdigit():
                end = i 
                break
        
        if end == 0:
            end = len(file)
        head = file[:start]
        number = file[start:end]
        tail = file[end:]
        answer.append(File(head, number, tail, org_idx))
        # break

    answer = sorted(answer, key=cmp_to_key(cmp))
    return ["".join([x.head, x.number, x.tail]) for x in answer]


if __name__ == "__main__":
    assert solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
    assert solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
    assert solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]) == ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]
    assert solution(["ab12", "ab1"]) == ["ab1", "ab12"]