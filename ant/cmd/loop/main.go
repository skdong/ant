package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main(){
	reload := make(chan bool, 1)
	reload <- true
	for <- reload{
		reload <- false
		fmt.Println("test")
		a := <- reload
		fmt.Printf("%v\n", a)
		reload <- false

		signals := make(chan os.Signal)
		signal.Notify(signals, os.Interrupt, syscall.SIGHUP,
			syscall.SIGTERM, syscall.SIGINT)
		go func(){
			select{
			case sig := <- signals:
				if sig == syscall.SIGHUP{
					log.Printf("Reloading test")
					<- reload
					reload <- true
				}
			}
		}
	}
}