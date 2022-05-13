-- To calculate (i + 2j + 3k) x (4i + 5j + 6k) do
-- lua cross_product.lua 1 2 3 4 5 6

function cross_product(v1, v2)
    return {
        i = v1.j * v2.k - v1.k * v2.j,
        j = v1.k * v2.i - v1.i * v2.k,
        k = v1.i * v2.j - v1.j * v2.i
    }
end

function print_vec(vec)
    print(tostring(vec.i) .. "i + " .. tostring(vec.j) .. "j + " .. tostring(vec.k) .. "k")
end

if #arg < 6 then
    print "Not enough arguments"
else
    vec1 = { i=arg[1], j=arg[2], k=arg[3] }
    vec2 = { i=arg[4], j=arg[5], k=arg[6] }
    print_vec(cross_product(vec1, vec2))
end
