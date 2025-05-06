import nslsii
from ophyd.signal import EpicsSignalBase


EpicsSignalBase.set_defaults(connection_timeout=10)
nslsii.configure_base(
    get_ipython().user_ns, 
    'xpeem',
    publish_documents_with_kafka=True,
    redis_url="info.esm.nsls2.bnl.gov",
    redis_prefix="xpeem-"
)
