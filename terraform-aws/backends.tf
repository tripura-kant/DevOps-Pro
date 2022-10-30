terraform {
  backend "s3" {
    bucket = "terraform-state-devopsthehardwaytripurakant"
    key    = "1ecr-terraform.tfstate"
    region = "us-east-1"
  }

}