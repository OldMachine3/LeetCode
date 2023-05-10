/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let tampung = init;
    for (const i of nums){
        tampung = fn(tampung, i)
    }
    return tampung;
};