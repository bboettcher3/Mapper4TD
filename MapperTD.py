import libmapper as mpr
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

def dstSigHandler(sig, event, id, val, timetag):
	me.parent().op("dstValues")[sig['name'], 1] = val

class MapperDevice:

	def __init__(self, ownerComp):

		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# Setup libmapper device and signals
		self.dev = mpr.Device(self.ownerComp.name)
		self.srcSigs = []
		self.dstSigs = []
		
		print("Creating mapper device: ", self.ownerComp.name)
		for chan in me.parent().op('inSources').chans():
			print("created source: ", chan.name)
			self.srcSigs.append(self.dev.add_signal(mpr.Direction.OUTGOING, chan.name, 1, mpr.Type.FLOAT, None, 0, 1))
		for chan in me.parent().op('dstSignalNames').chans():
			print("created dest: ", chan.name)
			self.dstSigs.append(self.dev.add_signal(mpr.Direction.INCOMING, chan.name, 1, mpr.Type.FLOAT, None, 0, 1, None, dstSigHandler))
		#mod(op("dstCallbacks")).initValues()

	def poll(self):
		self.dev.poll()
		return

	def sourceChanged(self, idx, value):
		self.srcSigs[idx].set_value(value)
		return
