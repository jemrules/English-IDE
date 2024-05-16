use pyo3::prelude::*;

// mod neural_network;

// use crate::neural_network::net;
// use crate::neural_network::neuron;
// use crate::neural_network::active_funcs::get_from_string;
// use crate::neural_network::active_funcs::get_deriv_from_string;

use std::env;
use std::fs;
use std::cmp::min;

// "../../.venv/Scripts/activate.bat"
// source ../../.venv/Scripts/activate
// maturin develop
// python3 -m maturin develop
// python -u ../EngIDE.py

/// Formats the sum of two numbers as string.
// #[pyfunction]
// fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
//     Ok((a + b).to_string())
// }
fn compare_correct(a: String, b:String) -> Vec<Vec<i16>> {
    let mut grid=vec![vec![0; b.len()+1];a.len()+1];
    // println!("{:?}",grid);
    for x in 0..a.len()+1 {
        for y in 0..b.len()+1 {
            if x==0 {
                grid[x][y]=y as i16;
            } else if y==0 {
                grid[x][y]=x as i16;
            } else {
                grid[x][y]=grid[x-1][y].min(grid[x-1][y-1]).min(grid[x][y-1]);
                if a.chars().nth(x-1).unwrap()!=b.chars().nth(y-1).unwrap() {
                    grid[x][y]+=1;
                }
            }

        }
    }
    grid
}

#[pyfunction]
fn autocorrect(word: String) -> PyResult<Vec<(String,i16)>> {
    let contents = fs::read_to_string("word_data/wordbank.txt")
        .expect("Unable to open Word Bank (word_data/wordbank.txt) file");
    let max_dist=3;
    let mut organized: Vec<(String,i16,i32)>=Vec::new();
    for qline in contents.lines() {
        let line=qline.split(";").collect::<Vec<&str>>()[0];
        let feq=qline.split(";").collect::<Vec<&str>>()[1].parse::<i32>().unwrap();
        if word.clone()==line.to_string() {
            continue;
        }
        let grid=compare_correct(word.clone(),line.to_string());
        let dist=grid[grid.len()-1][grid[0].len()-1] as i16;
        if dist<=max_dist {
            organized.push((line.to_string(),dist,feq));
        }
    }
    organized.sort_by_key(|k| k.1);
    organized=organized[0..min(20,organized.len())].to_vec();
    organized.sort_by_key(|k| k.2);
    let words=organized.iter().map(|a| (a.0.clone(),a.1.clone())).collect::<Vec<(String,i16)>>();
    Ok(words[0..min(20,words.len())].to_vec())
}

#[pyfunction]
fn compare_words(word1: String,word2: String) -> PyResult<Vec<Vec<i16>>> {
    Ok(compare_correct(word1,word2))
}

#[pyfunction]
fn autocomplete(subword: String,max_size: i16) -> PyResult<Vec<String>> {
    let contents = fs::read_to_string("word_data/wordbank.txt")
        .expect("Unable to open Word Bank (word_data/wordbank.txt) file");
    let mut valid_words: Vec<String>=contents.lines().filter(|a| a.starts_with(&subword)).map(|a| a.split(";").collect::<Vec<&str>>()[0].to_string()).collect();
    if valid_words.len()==0 {
        valid_words=vec![" ".to_string()];
    }
    match max_size {
        -1 => Ok(valid_words),
        _ => Ok(valid_words[0..min(max_size as usize,valid_words.len())].to_vec())
    }
}



#[pymodule]
#[pyo3(name = "english_rs")]
fn auto_features(_py: Python,m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(autocorrect, m)?)?;
    m.add_function(wrap_pyfunction!(compare_words, m)?)?;
    m.add_function(wrap_pyfunction!(autocomplete, m)?)?;
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