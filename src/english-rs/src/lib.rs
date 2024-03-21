use pyo3::prelude::*;

mod neural_network;

use crate::neural_network::neuron;
use crate::neural_network::active_funcs::get_from_string;
use crate::neural_network::active_funcs::get_deriv_from_string;

// "../../.venv/Scripts/activate.bat"

/// Formats the sum of two numbers as string.
// #[pyfunction]
// fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
//     Ok((a + b).to_string())
// }
#[pyfunction]
fn test_neuron(q_weights: Vec<f32>, q_bias: f32, q_activation: String) -> PyResult<String> {
    let mut n = neuron {
        weights: q_weights,
        bias: q_bias,
        activation: get_from_string(&q_activation),
        activation_deriv: get_deriv_from_string(&q_activation),
        value: 0.0,
        t_len: 0,
        w_derivs: vec![0.0],
        b_deriv: 0.0,
    };
    Ok(("Activation: ").to_string())
}



/// A Python module implemented in Rust.
#[pymodule]
fn english_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(test_neuron, m)?)?;
    Ok(())
}
