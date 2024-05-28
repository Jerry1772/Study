package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

func parseTime(aTime string) int {
	// hour:minute 형식의 string을 받아서 분단위로 parsing하는 함수
	sTime := strings.Split(aTime, ":")
	sHour, err := strconv.Atoi(sTime[0])
	if err != nil {
		panic(err)
	}
	sMinute, _ := strconv.Atoi(sTime[1])
	if err != nil {
		panic(err)
	}
	return 60*sHour + sMinute
}

func solution(fees []int, records []string) []int {
	var (
		sCarRecords = map[string]map[string][]string{}
		sAnswer     = []int{}
		sCarTime    = map[string]int{}
		sCarNumbers = []string{}
	)

	for _, sRecord := range records {
		sRecordSlice := strings.Split(sRecord, " ")
		sStartTime, sCarNumber, sIO := sRecordSlice[0], sRecordSlice[1], sRecordSlice[2]

		_, ok := sCarRecords[sCarNumber]
		if !ok {
			sCarRecords[sCarNumber] = map[string][]string{"IN": {}, "OUT": {}}
			sCarTime[sCarNumber] = 0
			sCarNumbers = append(sCarNumbers, sCarNumber)
		}
		sCarRecords[sCarNumber][sIO] = append(sCarRecords[sCarNumber][sIO], sStartTime)
	}

	for sCarNumber := range sCarRecords {
		if len(sCarRecords[sCarNumber]["IN"]) > len(sCarRecords[sCarNumber]["OUT"]) {
			sCarRecords[sCarNumber]["OUT"] = append(sCarRecords[sCarNumber]["OUT"], "23:59")
		}

		for _, sTime := range sCarRecords[sCarNumber]["IN"] {
			sCarTime[sCarNumber] -= parseTime(sTime)
		}

		for _, sTime := range sCarRecords[sCarNumber]["OUT"] {
			sCarTime[sCarNumber] += parseTime(sTime)
		}
	}

	sort.Slice(sCarNumbers, func(i, j int) bool {
		i_int, _ := strconv.Atoi(sCarNumbers[i])
		j_int, _ := strconv.Atoi(sCarNumbers[j])
		return i_int < j_int
	})

	for _, sCarNumber := range sCarNumbers {
		if sCarTime[sCarNumber] < fees[0] {
			sAnswer = append(sAnswer, fees[1])
		} else {
			sAnswer = append(sAnswer, fees[1]+int(math.Ceil(float64(sCarTime[sCarNumber]-fees[0])/float64(fees[2]))*float64(fees[3])))
		}
	}

	return sAnswer
}

func main() {
	var (
		fees    = []int{180, 5000, 10, 600}
		records = []string{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"}
	)
	fmt.Println(solution(fees, records))
}
