from math import ceil

class ParkingInfo():
    def __init__(
        self,
        number: str,
        in_time: str,
        state: bool = True, # True: 입차, False: 출차
        cml_time: int = 0
    ) -> None:
    
        self.number = number
        self.in_time = in_time
        self.state = state
        self.cml_time = cml_time

    def out(self, out_time:str) -> None:
        in_h, in_m = self.in_time.split(":")
        in_time_to_minute = int(in_h) * 60 + int(in_m)

        out_h, out_m = out_time.split(":")
        out_time_to_minute = int(out_h) * 60 + int(out_m)
        
        self.cml_time += out_time_to_minute - in_time_to_minute
        self.state = False

    
    def parking(self, in_time:str) -> None:
        self.in_time = in_time
        self.state = True

class ParkingArea():
    def __init__(
        self,
        fees: list,
    ) -> None:
        self.parking_infos = []
        self.fees = fees
    
    def find_info(self, number) -> int:
        for idx in range(len(self.parking_infos)):
            if self.parking_infos[idx].number == number:
                return idx

        return None

    def parking(self, number:str, in_time:str) -> None:
        idx = self.find_info(number)
        if idx != None:
            self.parking_infos[idx].parking(in_time)
        else: # 첫 주차
            parking_info = ParkingInfo(
                number=number,
                in_time=in_time,
                state=True,
                cml_time = 0
            )
            self.parking_infos.append(parking_info)

    def out(self, number:str, out_time: str) -> None:
        idx = self.find_info(number)
        self.parking_infos[idx].out(out_time)

    def calculate(self, cml_time:int) -> int:
        if cml_time <= self.fees[0]:
            return self.fees[1]
        return self.fees[1] + ceil((cml_time-self.fees[0])/self.fees[2]) * self.fees[3]

    def calculate_all(self) -> list:
        # 차량 번호대로 정렬
        self.parking_infos = sorted(self.parking_infos, key=lambda x: x.number)
        result = []
        for info in self.parking_infos: 
            if info.state: # 출차하지 않은 차량 처리
                info.out("23:59")
            result.append(self.calculate(info.cml_time))

        return result
    


def solution(fees, records):
    parking_area = ParkingArea(fees)

    for record in records:
        time, number, io = record.split(" ")
        if io == "IN":
            parking_area.parking(number, time)
        else:
            parking_area.out(number, time)

    return parking_area.calculate_all()


if __name__ == "__main__":
    assert (solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) == [14600, 34400, 5000]
    assert (solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) == [0, 591]
    assert (solution([1, 461, 1, 10], 	["00:00 1234 IN"])) == [14841]