resource "aws_dynamodb_table" "dna_data" {
  name         = var.dna_table_name
  hash_key     = "id"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }
}
