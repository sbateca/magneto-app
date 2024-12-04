variable "environment_name" {
  type = string
}

variable lambda_role_arn {
  type = string
}

variable "region" {
  type = string
}

variable "image_uri" {
  type = string
}

variable "image_tag" {
  type = string
}

variable "memory_size" {
  type = number
   default     = 256
  description = "Lambda memory size"
}

variable "timeout" {
  type = number
  default     = 10
  description = "Lambda timeout"
}

variable "api_gateway_execution_arn" {
  type = string
}

variable "magneto_dna_data_table" {
  type = string
}

