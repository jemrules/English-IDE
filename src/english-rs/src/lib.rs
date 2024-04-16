use pyo3::prelude::*;

// mod neural_network;

// use crate::neural_network::net;
// use crate::neural_network::neuron;
// use crate::neural_network::active_funcs::get_from_string;
// use crate::neural_network::active_funcs::get_deriv_from_string;

use std::env;
use std::fs;

// "../../.venv/Scripts/activate.bat"
// source ../../.venv/Scripts/activate
// maturin develop
// python3 -m maturin develop

/// Formats the sum of two numbers as string.
// #[pyfunction]
// fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
//     Ok((a + b).to_string())
// }
fn compare_correct(a: String, b:String) -> i16 {
    let mut grid=vec![vec![0; b.len()+1];a.len()+1];
    println!("{:?}",grid);
    0
}

#[pyfunction]
fn autocorrect(word: String) -> PyResult<Vec<String>> {
    let contents = fs::read_to_string("word_data/wordbank.txt")
        .expect("Unable to open Word Bank (word_data/wordbank.txt) file");
    let mut words: Vec<String> = Vec::new();
    for line in contents.lines() {
        words.push(line.to_string());
    }
    Ok(vec![word])
}


#[pymodule]
#[pyo3(name = "english_rs")]
fn auto_features(_py: Python,m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(autocorrect, m)?)?;
    Ok(())
}











// #[pyfunction]
// fn test_neuron(q_weights: Vec<f32>, q_bias: f32, q_activation: String) -> PyResult<String> {
//     // let mut n = neuron {
//     //     weights: q_weights,
//     //     bias: q_bias,
//     //     activation: get_from_string(&q_activation),
//     //     activation_deriv: get_deriv_from_string(&q_activation),
//     //     value: 0.0,
//     //     t_len: 0,
//     //     w_derivs: vec![0.0],
//     //     b_deriv: 0.0,
//     // };
//     let mut netw = net::network {
//         shape: vec![(5,"linear".to_string()),(5,"sigmoid".to_string())],
//         model: Vec::new(),
//     };
//     netw.model=netw.construct_shape();
//     Ok((netw.shape.iter().map(|a| a.1.clone()).collect::<Vec<String>>().join(" ")).to_string())
// }
// #[pymodule]
// fn nn(_py: Python, m: &PyModule) -> PyResult<()> {
//     m.add_function(wrap_pyfunction!(test_neuron, m)?)?;
//     Ok(())
// }

//  //          println!("{}",model.len());