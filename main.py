def predict(x, weight, bias):
    return weight*x + bias


def cost_function(x, y, weight, bias):
    num_points = len(x)
    total_error = 0.0
    for i in range(num_points):
        total_error += (y[i] - (weight*x[i] + bias))**2
    return total_error / num_points


def update_weights(x, y, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    num_points = len(x)

    for i in range(num_points):
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        weight_deriv += -2*x[i] * (y[i] - (weight*x[i] + bias))

        # -2(y - (mx + b))
        bias_deriv += -2*(y[i] - (weight*x[i] + bias))

    # We subtract because the derivatives point in direction of steepest ascent
    weight -= (weight_deriv / num_points) * learning_rate
    bias -= (bias_deriv / num_points) * learning_rate

    return [weight, bias]


def train(x, y, weight, bias, learning_rate, iters):
    cost_history = []

    for i in range(iters):
        weight,bias = update_weights(x, y, weight, bias, learning_rate)

        #Calculate cost for auditing purposes
        cost = cost_function(x, y, weight, bias)
        cost_history.append(cost)

        # Log Progress
        if i % 10 == 0:
            print("iter={:d}    weight={:.2f}    bias={:.4f}    cost={:.2}".format(i, weight, bias, cost))

    #return weight, bias, cost_history


with open("points.txt", "r") as file:
    data = str(file.read()).split(",")
    length = len(data)

    x = [None] * length
    y = [None] * length

    for i in range(length):
        x[i] = float(str(data[i]).split()[0])
        y[i] = float(str(data[i]).split()[1])


train(x, y, 10, 10, 1, 1000)
