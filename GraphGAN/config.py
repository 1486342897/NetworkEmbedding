import numpy as np
batch_size_dis = 64  # batch size for discriminator
batch_size_gen = 63  # batch size for generator
lambda_dis = 1e-5  # l2 loss regulation factor for discriminator
lambda_gen = 1e-5  # l2 loss regulation factor for generator
n_sample_dis = 20  # sample num for generator
n_sample_gen = 20  # sample num for discriminator
update_ratio = 1    # updating ratio when choose the trees
save_steps = 10

lr_dis = 1e-4  # learning rate for discriminator
lr_gen = 1e-3  # learning rate for discriminator

max_epochs = 50  # outer loop number
max_epochs_gen = 5  # loop number for generator
max_epochs_dis = 5  # loop number for discriminator

gen_for_d_iters = 10  # iteration numbers for generate new data for discriminator
max_degree = 0  # the max node degree of the network
model_log = "../log/iteration1/"

use_mul = False # control if use the multiprocessing when constructing trees
load_model = False  # if load the model for continual training
gen_update_iter = 200
window_size = 3
random_state = np.random.randint(0, 100000)
app = "link_prediction"
import_tree = False
tree_path = "../../data/input/trees"
train_filename = "../../data/input/toy-edges.txt"
test_filename = ""
test_neg_filename = ""
n_embed = 300
n_node = 9890
pretrain_emd_filename_d = "../../data/input/embed.txt"
pretrain_emd_filename_g = "../../data/input/embed.txt"
modes = ["dis", "gen"]
emb_filenames = ["../../data/output/toy_" + modes[0] + "_" + str(random_state) + ".emb",
                 "../../data/output/toy_" +  modes[1] + "_" + str(random_state) + ".emb"]
result_filename = "../../data/output/toy_" +  str(random_state) + ".txt"

# for mr_predict
test_data = "../../data/input/test.data"
crossmap = "../../data/input/pickled.model"
predict_type = ['w', 'l', 't']
node_dict = "../../data/input/node_dict111.txt"

