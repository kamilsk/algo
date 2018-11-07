package main

import (
	"reflect"
	"testing"
)

const format = `
expected %+v
obtained %+v`

func TestInsertion(t *testing.T) {
	tests := []struct {
		name     string
		array    []int
		expected []int
	}{
		{"case#01", []int{3, 1, 2}, []int{1, 2, 3}},
	}
	for _, test := range tests {
		tc := test
		t.Run(test.name, func(t *testing.T) {
			if obtained := insertion(tc.array); !reflect.DeepEqual(tc.expected, obtained) {
				t.Errorf(format, tc.expected, obtained)
			}
		})
	}
}
