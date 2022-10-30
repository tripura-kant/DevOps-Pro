###---networking/main.tf---


resource "random_integer" "random" {
  min = 1
  max = 100
}

resource "aws_vpc" "mtc_vpc" {
  cidr_block = var.vpc_cidr
}

