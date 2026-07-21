from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

comparison_count = 0  # Global counter

def min_max_dc(arr, low, high):
    global comparison_count
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    return overall_min, overall_max

def min_max_naive(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn: mn = x
        comps += 1
        if x > mx: mx = x
    return mn, mx, comps

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        # Get user input array
        arr_str = request.form.get("array")
        try:
            arr = list(map(int, arr_str.split(",")))
        except:
            output = "❌ Invalid input. Please enter comma-separated integers."
            arr = None

        if arr:
            global comparison_count
            comparison_count = 0
            mn, mx = min_max_dc(arr, 0, len(arr) - 1)
            dc_comps = comparison_count
            _, _, naive_comps = min_max_naive(arr)

            # Performance analysis
            perf_lines = []
            perf_lines.append(f'{"Size":>8} {"DC Comps":>12} {"Naive Comps":>14} {"Formula 3n/2-2":>16}')
            perf_lines.append('-' * 56)
            for size in [10, 100, 1000, 10000]:
                test_arr = [random.randint(1, 10000) for _ in range(size)]
                comparison_count = 0
                min_max_dc(test_arr, 0, len(test_arr) - 1)
                dc = comparison_count
                _, _, naive = min_max_naive(test_arr)
                formula = 3 * size // 2 - 2
                perf_lines.append(f'{size:>8} {dc:>12} {naive:>14} {formula:>16}')

            output = f"""
Array: {arr}<br>
Min: {mn}, Max: {mx}<br>
D&C Comparisons: {dc_comps}<br>
Naive Comparisons: {naive_comps}<br><br>
<pre>
{chr(10).join(perf_lines)}
</pre>
"""

    return render_template_string("""
        <h2>Min-Max Comparison (Divide & Conquer vs Naive)</h2>
        <form method="post">
            Enter array (comma-separated integers): <br>
            <input type="text" name="array" style="width:300px">
            <br><br>
            <input type="submit" value="Compute">
        </form>
        <hr>
        <div>{{output|safe}}</div>
    """, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
