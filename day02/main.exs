defmodule Main do
  defp insert_pair(cubedef, map) do
    [n, cube] = String.split(cubedef, " ")
    {n, _} = Integer.parse(n)

    case Map.get(map, cube) do
      nil -> Map.put(map, cube, n)
      m -> Map.put(map, cube, max(m, n))
    end
  end

  defp validate(map, name, n) do
    case Map.get(map, name) do
      nil -> false
      m -> m <= n
    end
  end

  def calc do
    case IO.gets("") do
      :eof ->
        0

      line ->
        (
          [head, tail] = line |> String.trim() |> String.split(": ")

          map =
            String.split(tail, "; ")
            |> List.foldr(
              Map.new(),
              fn cubespec, map ->
                String.split(cubespec, ", ") |> List.foldr(map, &insert_pair/2)
              end
            )

          map |> IO.inspect()

          if validate(map, "red", 12) && validate(map, "green", 13) && validate(map, "blue", 14) do
            String.split(head, " ") |> tl |> hd |> Integer.parse() |> elem(0)
          else
            0
          end
        ) + calc()
    end
  end
end

IO.puts(Main.calc() |> Integer.to_string())
