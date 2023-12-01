defmodule Main do
  def calc do
    case IO.gets("") do
      :eof ->
        0

      line ->
        (Regex.scan(
           ~r/[0-9]|on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e)/,
           line
         )
         |> Enum.flat_map(fn
           ["on"] ->
             [1]

           ["tw"] ->
             [2]

           ["thre"] ->
             [3]

           ["four"] ->
             [4]

           ["fiv"] ->
             [5]

           ["six"] ->
             [6]

           ["seve"] ->
             [7]

           ["eigh"] ->
             [8]

           ["nin"] ->
             [9]

           [c] ->
             case Integer.parse(c) do
               #  :error -> []
               {n, _} -> [n]
             end
         end)
         |> List.foldr(:empty, fn
           x, :empty -> {x, x}
           x, {_, b} -> {x, b}
         end)
         |> then(fn {x, y} -> 10 * x + y end)) + calc()

        #  |> then(fn x -> [x] end)) ++ calc()
    end
  end
end

IO.puts(Main.calc() |> Integer.to_string())
