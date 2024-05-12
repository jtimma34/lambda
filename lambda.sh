#!/bin/bash

#ensure terraform is setup in the environment to run this script 

terraform init

#apply the terraform script

terraform apply --auto-approve
