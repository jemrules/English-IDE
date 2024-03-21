// Activation Functions
pub mod active_funcs {
	pub fn get_from_string(s: &str) -> fn(f32) -> f32 {
		match s {
			"linear" => linear,
			"sigmoid" => sigmoid,
			"relu" => relu,
			"leaky_relu" => leaky_relu,
			"tanh" => tanh,
			_ => panic!("Invalid Activation Function"),
		}
	}
	pub fn get_deriv_from_string(s: &str) -> fn(f32) -> f32 {
		match s {
			"linear" => linear_deriv,
			"sigmoid" => sigmoid_deriv,
			"relu" => relu_deriv,
			"leaky_relu" => leaky_relu_deriv,
			"tanh" => tanh_deriv,
			_ => panic!("Invalid Activation Function Derivative"),
		}
	}


	pub fn linear(x: f32) -> f32 {
		x
	}
	pub fn linear_deriv(x: f32) -> f32 {
		1.0
	}
	pub fn sigmoid(x: f32) -> f32 {
		1.0 / (1.0 + (-x).exp())
	}
	pub fn sigmoid_deriv(x: f32) -> f32 {
		sigmoid(x) * (1.0 - sigmoid(x))
	}
	pub fn relu(x: f32) -> f32 {
		if x > 0.0 {
			x
		} else {
			0.0
		}
	}
	pub fn relu_deriv(x: f32) -> f32 {
		if x > 0.0 {
			1.0
		} else {
			0.0
		}
	}
	pub fn leaky_relu(x: f32) -> f32 {
		if x > 0.0 {
			x
		} else {
			0.01 * x
		}
	}
	pub fn leaky_relu_deriv(x: f32) -> f32 {
		if x > 0.0 {
			1.0
		} else {
			0.01
		}
	}
	pub fn tanh(x: f32) -> f32 {
		x.tanh()
	}
	pub fn tanh_deriv(x: f32) -> f32 {
		1.0 - tanh(x).powi(2)
	}
}

// Neuron
pub struct neuron {
	pub weights: Vec<f32>,
	pub bias: f32,
	pub activation: fn(f32) -> f32,
	pub activation_deriv: fn(f32) -> f32,

	pub value: f32,
	pub t_len: u16, // 65535 max
	pub w_derivs: Vec<f32>,
	pub b_deriv: f32,
}
impl Default for neuron {
	fn default() -> neuron {
		neuron {
			weights: vec![],
			bias: 0.0,
			activation: active_funcs::get_from_string("linear"),
			activation_deriv: active_funcs::get_deriv_from_string("linear"),

			value: 0.0,
			t_len: 0,
			w_derivs: vec![],
			b_deriv: 0.0,
		}
	}
}

impl neuron{
	pub fn f_prop(mut self,pre_layer: Vec<f32>) {
		self.value = self.bias;
		for i in 0..self.t_len {
			self.value += pre_layer[i as usize] * self.weights[i as usize];
		}
		self.value = (self.activation)(self.value);
	}
}

// Network
pub mod net {
	use crate::neuron;
	pub struct network {
		// amount, active_type
		pub shape: Vec<(u16,String)>,
		pub model: Vec<Vec<neuron>>,
	}
	impl Default for network {
		fn default() -> network {
			network {
				shape: vec![(0,"linear".to_string()),(0,"sigmoid".to_string())],
				model: Vec::new(),
			}
		}
	}
	impl network {
		fn construct_shape(mut self) -> Vec<Vec<neuron>> {
			for layer in 0..self.shape.len() {
				let mut c_layer: Vec<neuron> = Vec::new();
				for _ in 0..self.shape[layer].0 {
					c_layer.push(neuron {weights: vec![1.0,1.0], ..Default::default()});
				}
				self.model.push(c_layer);
			}
			return self.model;
		}
	}
}
