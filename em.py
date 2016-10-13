import random

# Implementation of "What is the expectation maximization algorithm?" by Chuong and Serafim
# http://www.nature.com/nbt/journal/v26/n8/full/nbt1406.html

# We have coin A and coin B, they have different probability land on head.
# For each experiment, we choose a coin and throw it 10 times, record the count of head and tail.
# We got data for 5 experiments, but didn't know which coin we throwed.
# Question: Get the probability land on head for coin A and B.
# Expected Result: Probability A = 0.8 B = 0.52 or A = 0.52, B = 0.80

# Experiment result: [Head_count, Tail_count]
EXPERIMENT_DATASET = [[5, 5], [9, 1], [8, 2], [4, 6], [7, 3]]


def maximum_likelihood_estimation(head_count, tail_count):
    """ Equation to get probability """
    return head_count / (head_count + tail_count)


if __name__ == "__main__":
    # Step 1. Guess probability A, B
    probability_A_estimate = random.random()
    probability_B_estimate = random.random()
    print("Guessed probability A = {0:.2f}, B = {1:.2f}".format(probability_A_estimate, probability_B_estimate))

    step = 0
    while True:
        # Step 2(E step). Get probability distribution from estimated parameter A and B
        print("Step {0}: ".format(step))
        heads_A = 0
        tails_A = 0
        heads_B = 0
        tails_B = 0
        for dataset_index in range(len(EXPERIMENT_DATASET)):
            heads = EXPERIMENT_DATASET[dataset_index][0]
            tails = EXPERIMENT_DATASET[dataset_index][1]

            Pro_A = ((1 - probability_A_estimate) ** tails) * (probability_A_estimate ** heads)
            Pro_B = ((1 - probability_B_estimate) ** tails) * (probability_B_estimate ** heads)

            Distribution_A = Pro_A / (Pro_A + Pro_B)
            Distribution_B = Pro_B / (Pro_A + Pro_B)

            # print("Dataset {0}: {1} Distribution A = {2:.2f}, B = {3:.2f}".format(dataset_index,
            #                                                                       EXPERIMENT_DATASET[dataset_index],
            #                                                                       Distribution_A, Distribution_B))
            heads_A += heads * Distribution_A
            tails_A += tails * Distribution_A
            heads_B += heads * Distribution_B
            tails_B += tails * Distribution_B
        # print("Coin A: Heads {0:.2f}, Tails {1:.2f}".format(heads_A, tails_A))
        # print("Coin B: Heads {0:.2f}, Tails {1:.2f}".format(heads_B, tails_B))

        # Step 3(M step). Get new probability for coin A and B
        new_probability_A_estimate = maximum_likelihood_estimation(heads_A, tails_A)
        new_probability_B_estimate = maximum_likelihood_estimation(heads_B, tails_B)
        print("New probability A = {0:.2f}, B = {1:.2f}".format(new_probability_A_estimate, new_probability_B_estimate))

        # Step 4: Repeat until converge
        if ((round(new_probability_A_estimate, 2) == round(probability_A_estimate, 2)) and (
                round(new_probability_B_estimate, 2) == round(probability_B_estimate, 2))):
            print("Converge, break...")
            break
        else:
            probability_A_estimate = new_probability_A_estimate
            probability_B_estimate = new_probability_B_estimate
        step += 1
    print("Final probability A = {0:.2f}, B = {1:.2f}".format(probability_A_estimate, probability_B_estimate))
