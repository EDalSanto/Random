class Polynomial:
	"""
	class with methods for performing algebriac operations on polynomials
	"""
	def __init__(self, coeffs):
		self.coeffs = coeffs 

	def coeff(self, i):
		return self.coeffs[len(self.coeffs) - 1 - i]

	def get_coeff(self):
		return self.coeffs

	def power_detective(self, loc):
		return len(self.coeffs) - loc - 1	

	def add(self, other):
		biggest = Polynomial(max(self.coeffs, other.coeffs, key=len))
		smallest = Polynomial(min(self.coeffs, other.coeffs, key=len))
		new_coeffs = [0] * len(biggest.get_coeff())
		diff_detective = abs(len(self.coeffs) - len(other.coeffs))
		new_coeffs[:diff_detective] = biggest.get_coeff()[:diff_detective]
		for cf in xrange(diff_detective, len(biggest.get_coeff())):
			biggest_val = biggest.coeff(biggest.power_detective(cf)) 
			smallest_val = smallest.coeff(smallest.power_detective(cf - diff_detective))
			new_coeffs[cf] = biggest_val + smallest_val	
		np = Polynomial(new_coeffs)
		return np

	def	mul(self, other):
		mult_dict = {}
		new_coeffs = []
		for cf_other in xrange(len(other.coeffs)):
			for cf_self in xrange(len(self.coeffs)): 
				other_coeff = other.coeff(other.power_detective(cf_other))
				self_coeff = self.coeff(self.power_detective(cf_self))
				new_coeff = other_coeff * self_coeff
				new_pow = other.power_detective(cf_other) + self.power_detective(cf_self)
				if (new_pow in mult_dict):
					mult_dict[new_pow] += new_coeff
				else:
					mult_dict[new_pow] = new_coeff
		for key in sorted(mult_dict, reverse=True):
			new_coeffs.append(mult_dict[key])	
		np = Polynomial(new_coeffs)
		return np

	def __str__(self):
		new_str = ""
		for i, cf in enumerate(self.coeffs):
			print cf
			new_str += str(cf)
			if (i < len(self.coeffs) - 2):
				new_str += (".000 z**%d + " % (self.power_detective(i)))
			elif (i < len(self.coeffs) - 1):
				new_str += (".000 z + ")
			else:
				new_str += (".000" )
		return new_str

	
if __name__=='__main__':
	p1 = Polynomial([1, 2, 3])
	p2 = Polynomial([100, 200, 300, 400])
#	p3 = p1.add(p2) 
#	print "test adding big to small: %s" % (p3.get_coeff() == [100, 201, 302, 403]) 
#	p4 = p2.add(p1)
#	print "test adding big to small: %s" % (p4.get_coeff() == [100, 201, 302, 403]) 
	p3 = p1.mul(p2)
	print "multiplied p1 by p2: %s" % (p3.get_coeff())
	print p3
