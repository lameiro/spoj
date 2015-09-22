import scala.io._

object Main {
  def solve(n: Int) = {
    var result = 0
    for (a <- 1 to n) {
      val new_rects = (n / a) - a + 1
      if (new_rects > 0) {
        result += new_rects
      }
    }
    result
  }

  def main(args: Array[String]) = {
    val line = StdIn.readInt()
    println(solve(line))
  }
}

