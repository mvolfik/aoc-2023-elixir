defmodule Main do
  def calc do
    case IO.gets("") do
      :eof ->
        0

      line ->
        (line
         |> String.graphemes()
         |> Enum.flat_map(fn c ->
           case Integer.parse(c) do
             :error -> []
             {n, _} -> [n]
           end
         end)
         |> List.foldr(:empty, fn
           x, :empty -> {x, x}
           x, {_, b} -> {x, b}
         end)
         |> then(fn {x, y} -> 10 * x + y end)) + calc()
    end
  end
end

IO.puts(Main.calc() |> Integer.to_string())
