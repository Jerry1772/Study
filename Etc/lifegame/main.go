package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"sync"
	"time"
)

type (
	Board struct {
		size       int
		board      [][]int
		next_board [][]int
		sleep_time float64
	}

	Config struct {
		SleepTime float64 `json:"sleep_time"`
		BoardSize int     `json:"board_size"`
		PointX    []int   `json:"point_x"`
		PointY    []int   `json:"point_y"`
		PrintIter int     `json:"print_iter"`
		CharAlive string  `json:"alive_char"`
		CharDead  string  `json:"dead_char"`
	}
)

func (b *Board) setSize(size int) {
	b.size = size
	for a := 0; a < size; a++ {
		b.board = append(b.board, []int{})
		b.next_board = append(b.next_board, []int{})
		for c := 0; c < size; c++ {
			b.board[a] = append(b.board[a], 0)
			b.next_board[a] = append(b.next_board[a], 0)
		}
	}
}

func (b *Board) setSleep(sleep float64) {
	b.sleep_time = sleep
}

func (b Board) print(count int, t, f string) {
	for i := 0; i < count; i++ {
		fmt.Print("\033[H\033[2J")
		fmt.Printf("current count: %d\n", i+1)

		for _, row := range b.board {
			for _, val := range row {
				val_conv := t
				if val == 0 {
					val_conv = f
				}
				fmt.Printf("%s ", val_conv)
			}
			fmt.Println()
		}
		b.getNextGen()
		time.Sleep(time.Duration(b.sleep_time*1000) * time.Millisecond)
	}
}

func (b *Board) getNeighbor(r, c int) int {
	sCount := 0
	for nr := r - 1; nr <= r+1; nr++ {
		if !(0 <= nr) || !(nr < b.size) {
			continue
		}
		for nc := c - 1; nc <= c+1; nc++ {
			if !(0 <= nc) || !(nc < b.size) {
				continue
			} else if nr == r && nc == c {
				continue
			} else if b.board[nr][nc] == 1 {
				sCount += 1
			}
		}
	}
	return sCount
}

func (b *Board) getNextGen() {
	for r := 0; r < b.size; r++ {
		for c := 0; c < b.size; c++ {
			sCount := b.getNeighbor(r, c)
			if b.board[r][c] == 0 && sCount == 3 {
				b.next_board[r][c] = 1
			} else if b.board[r][c] == 1 && (sCount == 2 || sCount == 3) {
				b.next_board[r][c] = 1
			} else {
				b.next_board[r][c] = 0
			}
		}
	}
	for r := 0; r < b.size; r++ {
		for c := 0; c < b.size; c++ {
			b.board[r][c] = b.next_board[r][c]
		}
	}
}

func (b *Board) AddPoint(r, c int) {
	b.board[r][c] = 1
}

func (b *Board) AddPoints(rs, cs []int) {
	if len(rs) != len(cs) {
		fmt.Println("x,y 좌표 갯수 다름")
		os.Exit(1)
	}

	for i := range rs {
		b.AddPoint(rs[i], cs[i])
	}
}

func main() {
	var (
		sConfig Config
		wg      sync.WaitGroup = sync.WaitGroup{}
	)

	sData, err := os.Open("./config.json")
	if err != nil {
		fmt.Println("Failed to open config file")
		os.Exit(1)
	}
	sByte, _ := io.ReadAll(sData)
	json.Unmarshal(sByte, &sConfig)

	wg.Add(2)

	go func() {

		sBoard := Board{}

		sBoard.setSize(sConfig.BoardSize)
		sBoard.setSleep(sConfig.SleepTime)

		sBoard.AddPoints(sConfig.PointX, sConfig.PointY)

		sBoard.print(sConfig.PrintIter, sConfig.CharAlive, sConfig.CharDead)

		wg.Done()
	}()

	go func() {
		for {
			input := bufio.NewScanner(os.Stdin)
			input.Scan()

			if input.Text() == "q" {
				wg.Done()
				break
			}
		}
		os.Exit(0)
	}()
	wg.Wait()

}
