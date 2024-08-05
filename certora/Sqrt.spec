/*
 * Certora Formal Verification Spec of the SQRT function
 */ 

// We can also do "using" like a library in Certora
// using CompactCodeBase as math_masters; 

// methods {
//     function mathMastersSqrt(uint256) external returns uint256 envfree;
//     function uniSqrt(uint256) external returns uint256 envfree;
// }
methods {
    function mathMastersSqrtTopHalf(uint256) external returns uint256 envfree;
    function solmateSqrtTopHalf(uint256) external returns uint256 envfree;
}


// rule uniSqrtMatchesMathMastersSqrt(uint256 x) {
//     assert(math_masters.mathMastersSqrt(x) == math_masters.uniSqrt(x));
// }

rule solmateSqrtTopHalfMatchesMathMastersSqrtTopHalf(uint256 x) {
    assert(mathMastersSqrtTopHalf(x) == solmateSqrtTopHalf(x));
}