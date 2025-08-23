from netapp_ontap import config, HostConnection, NetAppRestError
from netapp_ontap.resources import Volume

config.CONNECTION = HostConnection(
    host="192.168.241.133",       # Replace with your cluster IP
    username="admin",             # Replace with your credentials
    password="Deepak@4",
    verify=False                  # Disable SSL verification for self-signed certs
    )






volume = Volume(
    name="vol_data_01",               # Volume name
    svm={"name": "svm1"},      # SVM name
    aggregates=[{"name": "aggr_test"}],   # Aggregate name
    size=1073741824,                  # Size in bytes (1GB)
    space_guarantee="volume",         # Optional: reserve space
    security_style="unix",            # Optional: UNIX/NFS style
    comment="Created via Python script"
)

# Step 3: Create the volume
try:
    volume.post()
    print(f"✅ Volume '{volume.name}' created successfully.")
except NetAppRestError as err:
    print(f"❌ Failed to create volume: {err}")
