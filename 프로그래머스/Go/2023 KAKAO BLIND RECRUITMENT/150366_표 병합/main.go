package main

import (
	"strconv"
	"strings"
)

type Cell struct {
	r          int
	c          int
	val        *string
	mergedWith map[*Cell]bool
}

func (c *Cell) update(newVal *string) {
	for cell := range c.mergedWith {
		cell.val = newVal
	}
	c.val = newVal
}

func (c *Cell) addMergedWith(targets []*Cell) {
	for _, target := range targets {
		if target != c {
			c.mergedWith[target] = true
		}
	}
}

type CellManager struct {
	board  [][]*Cell
	answer []string
}

func NewCellManager() *CellManager {
	cm := &CellManager{
		board:  make([][]*Cell, 51),
		answer: make([]string, 0),
	}
	for r := range cm.board {
		cm.board[r] = make([]*Cell, 51)
		for c := range cm.board[r] {
			cm.board[r][c] = &Cell{r: r, c: c, val: nil, mergedWith: make(map[*Cell]bool)}
		}
	}
	return cm
}

func (manager *CellManager) update(r, c int, value *string) {
	cell := manager.board[r][c]
	cell.update(value)
}

func (manager *CellManager) updateAll(value1, value2 *string) {
	for _, row := range manager.board {
		for _, cell := range row {
			if cell.val != nil && *cell.val == *value1 {
				cell.update(value2)
			}
		}
	}
}

func (manager *CellManager) merge(r1, c1, r2, c2 int) {
	if r1 == r2 && c1 == c2 {
		return
	}
	cell1, cell2 := manager.board[r1][c1], manager.board[r2][c2]
	val := cell1.val
	if val == nil {
		val = cell2.val
	}
	mergedWith := []*Cell{cell1, cell2}
	for cell := range cell1.mergedWith {
		mergedWith = append(mergedWith, cell)
	}
	for cell := range cell2.mergedWith {
		if cell != cell1 {
			mergedWith = append(mergedWith, cell)
		}
	}
	for _, cell := range mergedWith {
		cell.addMergedWith(mergedWith)
		cell.val = val
	}
}

func (manager *CellManager) unmerge(r, c int) {
	cell := manager.board[r][c]
	for mergedCell := range cell.mergedWith {
		mergedCell.val = nil
		mergedCell.mergedWith = make(map[*Cell]bool)
	}
	cell.mergedWith = make(map[*Cell]bool)
}

func (manager *CellManager) print(r, c int) {
	cell := manager.board[r][c]
	if cell.val == nil {
		manager.answer = append(manager.answer, "EMPTY")
	} else {
		manager.answer = append(manager.answer, *cell.val)
	}
}

func solution(commands []string) []string {
	manager := NewCellManager()
	for _, command := range commands {
		splitCmd := strings.Split(command, " ")
		switch splitCmd[0] {
		case "UPDATE":
			if len(splitCmd) == 4 {
				r, _ := strconv.Atoi(splitCmd[1])
				c, _ := strconv.Atoi(splitCmd[2])
				val := splitCmd[3]
				manager.update(r, c, &val)
			} else {
				val1 := splitCmd[1]
				val2 := splitCmd[2]
				manager.updateAll(&val1, &val2)
			}
		case "MERGE":
			r1, _ := strconv.Atoi(splitCmd[1])
			c1, _ := strconv.Atoi(splitCmd[2])
			r2, _ := strconv.Atoi(splitCmd[3])
			c2, _ := strconv.Atoi(splitCmd[4])
			manager.merge(r1, c1, r2, c2)
		case "UNMERGE":
			r, _ := strconv.Atoi(splitCmd[1])
			c, _ := strconv.Atoi(splitCmd[2])
			manager.unmerge(r, c)
		case "PRINT":
			r, _ := strconv.Atoi(splitCmd[1])
			c, _ := strconv.Atoi(splitCmd[2])
			manager.print(r, c)
		}
	}
	return manager.answer
}
