function shortestPalindrome(s: string): string {
    let j = 0
    for(let i = 0 ; i < s.length; i++){
        if(s[s.length - i - 1] === s[j]){
            j++
        }
    }
    if(j==s.length)
        return s

    let p = s.substring(j);
    p = p.split('').reverse().join('');
    
    return (p + shortestPalindrome(s.substring(0, j)) + s.substring(j))
};