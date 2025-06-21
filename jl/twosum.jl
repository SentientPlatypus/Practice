



function twosum(a::Array{Int,1}, target::Int)
    mp = Dict{Int, Int}()

    for i in 1:length(a)
        comp = target - a[i]
        if haskey(mp, comp)
            return [mp[comp], i]
        end
        mp[a[i]] = i
    end
    return nothing
end






a = map(x -> parse(Int, x), split(readline()))
target = parse(Int, readline())
println(twosum(a, target))




