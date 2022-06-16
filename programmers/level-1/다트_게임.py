
def solution(dartResult):
    
    dartResult += " "
    exp = ["", "S", "D", "T"]
    game = []
    game_index = 0
    index = 0
    score = ""
    while len(dartResult) > 1:

        try:
            print(dartResult, score, index, dartResult[index])
        except:
            print(index)
        if dartResult[index].isdigit() or dartResult[index] == " ":
            if index > 1:
                game.append(int(score))
                print(game)
                game_index += 1
                dartResult = dartResult[index:]
                index = 0
                score = ""
                continue
            else:
                score += dartResult[index]

        if dartResult[index] in exp:
            score = str(int(score) ** exp.index(dartResult[index]))

        if dartResult[index] in ["#", "*"]:
            if dartResult[index] == "#":
                score = str(int(score) * -1)

            if dartResult[index] == "*":
                if game_index > 0:
                    game[game_index-1] *= 2
                score = str(int(score) * 2)

        index += 1
    
    return sum(game)

if __name__ == "__main__":
    dartResults = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
    print([solution(dartResult) for dartResult in dartResults])

    