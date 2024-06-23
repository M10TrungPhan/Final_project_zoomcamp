variable "credentials" {
    description = "My credentials"
    default =  "../keys/my_cred.json"
}

variable "project" {
  description = "Poject ID"
  default = "project-de-pnt"
}

variable "region" {
  description = "Region run service"
  default = "ASIA-SOUTHEAST1"
}

variable "location" {
  description = "Project Location"
  default     = "ASIA-SOUTHEAST1"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset name"
  default     = "final_project_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "final_project_pnt"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}