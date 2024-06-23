provider "google" {
    credentials = file(var.credentials)
    project = var.project
    region = var.region
}

resource "google_storage_bucket" "final_project_pnt" {
    name = var.gcs_bucket_name
    location = var.location

    storage_class = var.gcs_storage_class
    uniform_bucket_level_access = true
    force_destroy = true

    versioning {
      enabled = true
    }

    lifecycle_rule {
      action {
        type = "Delete"
      }
      condition {
        age = 5 
      }
    }

}

resource "google_bigquery_dataset" "final_prokect_dataset" {
    dataset_id = var.bq_dataset_name
    location = var.location
  
}

