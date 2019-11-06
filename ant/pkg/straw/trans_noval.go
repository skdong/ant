package straw

import (
	"os"
	"io"
	"bufio"
	"fmt"
	"strings"
	"github.com/axgle/mahonia"
)

func TransNoval(){
	file, error := os.Open("test.txt")
	if error != nil{
		fmt.Println(error)
		return
	}
	defer file.Close()

	enc := mahonia.NewDecoder("gbk")
	br := bufio.NewReader(file)
	content := ""
	for{
		a, _, c := br.ReadLine()
		if c == io.EOF{
			break
		}
		line := enc.ConvertString(string(a))
		if strings.Contains(line, "正文"){
			line = strings.Replace(line, "(", "第", 1)
			line = strings.Replace(line, "（", "第", 1)
			line = strings.Replace(line, ")", "章 ", 1)
			line = strings.Replace(line, "）", "章 ", 1)
		}
		content = content+"\n"+line
	}
	target, error := os.OpenFile("test.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0644)
	if error != nil{
		fmt.Println(error)
		return
	}
	defer target.Close()
	if _, error := target.WriteString(content); error != nil{
		fmt.Println(error)
	}
		//fmt.Println(string(buf))

}